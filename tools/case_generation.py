from execute import *
import threading
def calc_exec_time(ts): # Hodges--Lehmann estimator
    ts = np.array(ts) / 2.
    ts = ts[None, :] + ts[:, None]
    ts = ts[np.tril_indices_from(ts)]
    return np.median(ts)


def calc_eff(elapsed, ref, timeout):
    return max(0., timeout - elapsed) / (timeout - ref)

def calc_eff_at_k(e, k): # numerically stable implementation
    n = len(e)
    lbd = [k / n]
    k_ = k - 1
    for r in range(n - 1, k_, -1):
        lbd.append(lbd[-1] * (1 - k_ / r))
    lbd = np.flip(lbd)
    e = np.sort(e)[k_ :]
    return (lbd * e).sum()
class Test: # a testcode case
    def __init__(self, input = None, answer = None, ref = None):
        self.input = input
        self.answer = answer
        self.ref = ref # reference execution time

class Refs: # references for efficiency evaluation
    def __init__(self, tests, hardness):
        neg_inf = float('-inf')
        self.refs = [neg_inf] * len(hardness)
        self.ref_max = neg_inf
        self.lid = None
        self.cid = None
        # finds the longest reference execution time for calibration
        for j, (size, tests_j) in enumerate(tests):
            if hardness[j]:
                for k, test in enumerate(tests_j):
                    if self.refs[j] < test.ref:
                        self.refs[j] = test.ref
                        if self.ref_max < test.ref:
                            self.ref_max = test.ref
                            self.lid = j
                            self.cid = k

class Evaluator:
    TPL_MAKE = '''%s
%s
random.seed(%d)
__input = generate_input(size = %d, lid = %d, cid = %d)
''' # (disprompt, generator, seed, size)
    TPL_RUN = '''%s
%s
__t0 = time.time()
__output = %s(*__input)
__t1 = time.time()
''' # (disprompt, solution, entry_point)
    TPL_RUN2 = """%s
__t0 = time.time()
__output = %s(*__input)
__t1 = time.time()"""
    TPL_TEST = '''%s
    pass
%s
__accepted = __check(__input, __answer, __output)
'''
    def __init__(self, problems, subset, n_tests: int, n_reps: int, hardness, memory_giga: float, timeout_factor: float, tolerence_sec: float, seed: int,fname:str):
        self.problems = pd.read_csv(problems)
        self.n_problems = self.problems.shape[0]
        self.subset = list(range(self.n_problems)) if subset is None else sorted(set(subset))
        self.lock = threading.Lock()
        with self.lock:
            self.n_tests = n_tests
        self.hardness = np.array(hardness)
        self.n_levels = len(self.hardness)
        self.n_reps = [n_reps if self.hardness[j] else 1 for j in
                       range(self.n_levels)]  # no need to repeat if it does not count into the efficiency score
        self.memory = memory_giga * (1024 ** 3)
        self.timeout_factor = timeout_factor
        self.tolerence_sec = tolerence_sec
        with self.lock:
            self.tests = [[] for i in range(self.n_problems)]
        self.seed = seed
        #添加对mbpp测试集的支持
        self.load_tests(fname)

    def load_tests(self, fname):
        with self.lock:
            if osp.isfile(fname):
                with open(fname, 'rb') as fi:
                    self.tests, self.refs = pickle.load(fi)
                print('Tests loaded from', fname, flush = True)
                return True
            else:
                return False

    def compute_refs(self, i):
        try:# computes the calibration factor of of execution time
            problem = self.problems.iloc[i]
            with self.lock:
                tests = self.tests[i]
                if len(tests) == 0:
                    return None
                for j in range(len(tests)):
                    if self.hardness[j]:
                        for k in range(len(tests[j][-1])):
                            test = tests[j][-1][k]
                            n_reps = self.n_reps[j]
                            elapsed = [None for rep in range(n_reps)]
                            for rep in range(n_reps):
                                scope = dict(time = time, __input = deepcopy(test.input)) # in case that the code modifies the input
                                unsafe_execute(self.TPL_RUN % (problem.prompt, problem.reference_solution, problem.entry_point), scope) # assuming that the reference solution is error-free
                                elapsed[rep] = scope['__t1'] - scope['__t0']
                            test.ref = calc_exec_time(elapsed).item()
            return Refs(tests = tests, hardness = self.hardness)
        except:
            return None

    def zero_effs(self):
        return [0. for j in range(self.n_levels)]

    def evaluate_new(self):
        pass

    def case_gen(self):
        result_dict = {}

        for i in range(0,164):
            try:
                problem = self.problems.iloc[i]
                tests = self.tests[i][1][-1]
                test_case = f"print({problem.entry_point.strip()}{str(tests[-1].input)})"
                result_dict[str(i)] = test_case
            except:
                print(i)
                pass

        return result_dict



    def evaluate1(self, i, code, refs, verbose): # evaluates one code sample
        problem = self.problems.iloc[i]
        timeout = self.timeout_factor * refs.ref_max
        effs = []
        elapsed_list = []
        tests_case = {}
        with self.lock:
            for j, (size, tests) in enumerate(self.tests[i]):
                n_reps = self.n_reps[j]
                level_elapsed = []
                level_break = False
                #写入test_case

                for k, test in enumerate(tests):
                    elapsed = [None for rep in range(n_reps)]
                    for rep in range(n_reps):
                        scope = dict(time = time, input = None, print = None, __input = deepcopy(test.input)) # in case that the code modifies the input


                        try:
                            code_executed = self.TPL_RUN2 % (code.strip(), problem.entry_point.strip())
                            scope['__input'] = test.input
                            scope['__answer'] = test.answer
                            unsafe_timed_execute(code_executed, scope,timeout + self.tolerence_sec)
                            unsafe_execute(self.TPL_TEST % (problem.prompt, problem.checker), scope)
                        except TimeoutException as e:
                            if verbose:
                                print(f'[problem={i}, level={j}, case={k}] Time Limit Exceeded (size={size}, timeout={timeout:.4f})')####
                            error_msg = {f"The wrong case with time limit exceeded,timeout={timeout:.4f}": {"input": scope['__input'], "output": scope['__output'],"real_answer": scope['__answer']}}
                            level_break = True
                            return False,error_msg,""
                            break
                        except MemoryError as e:
                            if verbose: print(f'[problem={i}, level={j}, case={k}] Out of Memory (size={size})')####
                            level_break = True
                            break
                        except OverflowError as e:
                            if verbose: print(f'[problem={i}, level={j}, case={k}] Overflow Error (size={size})')####
                            level_break = True
                            break
                        except KeyboardInterrupt as e:
                            raise e
                        except BaseException as e:
                            if verbose:
                                print(f'[problem={i}, level={j}, case={k}] {type(e)}: {e}')####
                            error_msg = {
                            f"The wrong case_{type(e)}: {e}": {"input": scope['__input'],
                                                         "real_answer": scope['__answer']}}
                            return False, error_msg, ""
                        else:
                            if '__accepted' in scope and scope['__accepted']:
                                elapsed[rep] = scope['__t1'] - scope['__t0']
                            else:
                                if verbose: print(f'[problem={i}, level={j}, case={k}] Wrong output')####
                                error_msg = {"The wrong case":{"input":scope['__input'],"output":scope['__output'],"real_answer":scope['__answer']}}
                                return False, error_msg,""
                    if level_break:
                        break
                    else:
                        level_elapsed.append(calc_exec_time(elapsed).item())
                elapsed_list.append(level_elapsed)
                if level_break:
                    break
                else:
                    effs.append(calc_eff(elapsed = max(level_elapsed), ref = refs.refs[j], timeout = timeout))
            if j == 0 and level_break:
                return False, self.zero_effs(), elapsed_list
            for j in range(len(effs), self.n_levels):
                effs.append(0.)
            return True, "", elapsed_list

    def evaluate2(self, i, code, refs, verbose): # evaluates one code sample
        problem = self.problems.iloc[i]
        timeout = self.timeout_factor * refs.ref_max
        effs = []
        elapsed_list = []
        for j, (size, tests) in enumerate(self.tests[i]):
            n_reps = self.n_reps[j]
            level_elapsed = []
            level_break = False
            for k, test in enumerate(tests):
                elapsed = [None for rep in range(n_reps)]
                for rep in range(n_reps):
                    scope = dict(time = time, input = None, print = None, __input = deepcopy(test.input)) # in case that the code modifies the input
                    try:
                        # unsafe_execute(self.TPL_RUN % (problem.disprompt, code, problem.entry_point), scope, self.memory, timeout + self.tolerence_sec)
                        scope['__input'] = test.input
                        scope['__answer'] = test.answer # to prevent the code reading the answer
                        unsafe_execute(self.TPL_TEST % (problem.prompt, problem.checker), scope) # assuming that the checker does not modify the input
                    except TimeoutException as e:
                        if verbose: print(f'[problem={i}, level={j}, case={k}] Time Limit Exceeded (size={size}, timeout={timeout:.4f})')####
                        level_break = True
                        break
                    except MemoryError as e:
                        if verbose: print(f'[problem={i}, level={j}, case={k}] Out of Memory (size={size})')####
                        level_break = True
                        break
                    except OverflowError as e:
                        if verbose: print(f'[problem={i}, level={j}, case={k}] Overflow Error (size={size})')####
                        level_break = True
                        break
                    except KeyboardInterrupt as e:
                        raise e
                    except BaseException as e:
                        if verbose: print(f'[problem={i}, level={j}, case={k}] {type(e)}: {e}')####
                        return False, self.zero_effs(), elapsed_list
                    else:
                        if '__accepted' in scope and scope['__accepted']:
                            elapsed[rep] = scope['__t1'] - scope['__t0']
                        else:
                            if verbose: print(f'[problem={i}, level={j}, case={k}] Wrong output')####
                            return False, self.zero_effs(), elapsed_list
                if level_break:
                    break
                else:
                    level_elapsed.append(calc_exec_time(elapsed).item())
            elapsed_list.append(level_elapsed)
            if level_break:
                break
            else:
                effs.append(calc_eff(elapsed = max(level_elapsed), ref = refs.refs[j], timeout = timeout))
        if j == 0 and level_break:
            return False, self.zero_effs(), elapsed_list
        for j in range(len(effs), self.n_levels):
            effs.append(0.)
        return True, effs, elapsed_list


    def evaluate(self, codes, k, save_name = None, verbose = False): # evaluates all code samples
        if isinstance(k, int):
            k = [k]
        min_codes = min(len(codes[i]) for i in self.subset)
        k = sorted({k_ for k_ in k if k_ <= min_codes})
        passes = [0. for k_ in k]
        effs = [0. for k_ in k]
        passes_ = dict()
        effs_ = dict()
        elapsed_ = dict()
        tbar = tqdm(self.subset, desc = 'Evaluating')
        gc.collect()
        for i in tbar:
            tbar.set_description(f'Evaluating #{i}')
            refs = self.compute_refs(i = i)
            n_levels = len(self.tests[i])
            problem_passes = []
            problem_effs = []
            problem_elapsed = []
            for code in codes[i]:
                passed, code_effs, code_elapsed = self.evaluate1(i = i, code = code, refs = refs, verbose = verbose)
                problem_passes.append(passed)
                problem_effs.append(code_effs)
                problem_elapsed.append(code_elapsed)
            passes_[i] = deepcopy(problem_passes)
            effs_[i] = deepcopy(problem_effs)
            elapsed_[i] = problem_elapsed
            for j, k_ in enumerate(k):
                passes[j] += calc_pass_at_k(n = len(problem_passes), c = sum(problem_passes), k = k_)
                effs[j] += calc_eff_at_k(e = np.average(problem_effs, axis = 1, weights = self.hardness), k = k_)
        metrics = dict()
        n_problems = len(self.subset)
        for k_, pass_k in zip(k, passes):
            metrics[f'pass@{k_}'] = pass_k / n_problems
        for k_, eff_k in zip(k, effs):
            metrics[f'eff@{k_}'] = eff_k / n_problems
        if save_name is not None:
            with open(f'{save_name}~passes.json', 'w') as fo:
                json.dump(passes_, fo)
            with open(f'{save_name}~effs.json', 'w') as fo:
                json.dump(effs_, fo)
            with open(f'{save_name}~elapsed.json', 'w') as fo:
                json.dump(elapsed_, fo)
            with open(f'{save_name}~metrics.json', 'w') as fo:
                json.dump(metrics, fo)
        return metrics

def calc_pass_at_k(n, c, k):  # from the HumanEval paper
    if n - c < k: return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

# evaluator.make_tests()
# code_evaluator = CodeEvaluator(code=user_code)
# result = code_evaluator.evaluate()