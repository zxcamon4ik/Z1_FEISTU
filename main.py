import unittest
import subprocess
import os 


project_root = os.path.dirname(os.path.abspath(__file__))

class TesterZ(unittest.TestCase):
    def make_run(self, scenario, number):
        path = os.path.join(project_root, f"cases/tests/scenar_{scenario}/input{number}.txt")
        with open(path, "r") as f:
            content = f.read()
        subprocess.run(
            ["make", "create", f"INPUT={content}", f"NAME=output{scenario}.{number}.txt"],
            cwd=project_root,
            capture_output=True,
            text=True
        )

    def test_01(self):
        for i in range(8):
            self.make_run(1, i + 1)
            
            content_path = os.path.join(project_root, f"cases/tests/scenar_1/output{i+1}.txt")
            result_path = os.path.join(project_root, f"cases/local/output1.{i+1}.txt")
            
            with open(content_path, "r") as f:
                expected = f.read()
            with open(result_path, "r") as f:
                result = f.read().rstrip("\n")
            
            try:
                self.assertMultiLineEqual(expected, result, f"Test {i+1} failed")
            except AssertionError as e:
                print(f"\033[91mScenario 1 Case {i+1}: FAILURE\033[0m")
                raise e
            else:
                print(f"\033[92mScenario 1 Case {i+1}: SUCCESS\033[0m")

    def test_02(self):
        print("\n")
        for i in range(4):
            self.make_run(2, i + 1)
            
            content_path = os.path.join(project_root, f"cases/tests/scenar_2/output{i+1}.txt")
            result_path = os.path.join(project_root, f"cases/local/output2.{i+1}.txt")
            
            with open(content_path, "r") as f:
                expected = f.read()
            with open(result_path, "r") as f:
                result = f.read().rstrip("\n")
            
            try:
                self.assertMultiLineEqual(expected, result, f"Test {i+1} failed")
            except AssertionError as e:
                print(f"\033[91mScenario 2 Case {i+1}: FAILURE\033[0m")
                raise e
            else:
                print(f"\033[92mScenario 2 Case {i+1}: SUCCESS\033[0m")

    def test_03(self):
        print("\n")
        for i in range(7):
            self.make_run(3, i + 1)
            
            content_path = os.path.join(project_root, f"cases/tests/scenar_3/output{i+1}.txt")
            result_path = os.path.join(project_root, f"cases/local/output3.{i+1}.txt")
            
            with open(content_path, "r") as f:
                expected = f.read().rstrip()
            with open(result_path, "r") as f:
                result = f.read().rstrip()
            
            try:
                self.assertMultiLineEqual(expected, result, f"Test {i+1} failed")
            except AssertionError as e:
                print(f"\033[91mScenario 3 Case {i+1}: FAILURE\033[0m")
                raise e
            else:
                print(f"\033[92mScenario 3 Case {i+1}: SUCCESS\033[0m")

    def test_04(self):
        print("\n")
        for i in range(7):
            self.make_run(4, i + 1)
            
            content_path = os.path.join(project_root, f"cases/tests/scenar_4/output{i+1}.txt")
            result_path = os.path.join(project_root, f"cases/local/output4.{i+1}.txt")
            
            with open(content_path, "r") as f:
                expected = f.read().rstrip()
            with open(result_path, "r") as f:
                result = f.read().rstrip()
            
            try:
                self.assertMultiLineEqual(expected, result, f"Test {i+1} failed")
            except AssertionError as e:
                print(f"\033[91mScenario 4 Case {i+1}: FAILURE\033[0m")
                raise e
            else:
                print(f"\033[92mScenario 4 Case {i+1}: SUCCESS\033[0m")
        
    def test_05(self):
        print("\n")
        for i in range(9):
            self.make_run(5, i + 1)
            
            content_path = os.path.join(project_root, f"cases/tests/scenar_5/output{i+1}.txt")
            result_path = os.path.join(project_root, f"cases/local/output5.{i+1}.txt")
            
            with open(content_path, "r") as f:
                expected = f.read().rstrip()
            with open(result_path, "r") as f:
                result = f.read().rstrip()
            
            try:
                self.assertMultiLineEqual(expected, result, f"Test {i+1} failed")
            except AssertionError as e:
                print(f"\033[91mScenario 5 Case {i+1}: FAILURE\033[0m")
                raise e
            else:
                print(f"\033[92mScenario 5 Case {i+1}: SUCCESS\033[0m")
    
    def test_06(self):
        print("\n")
        for i in range(9):
            self.make_run(6, i + 1)
            
            content_path = os.path.join(project_root, f"cases/tests/scenar_6/output{i+1}.txt")
            result_path = os.path.join(project_root, f"cases/local/output6.{i+1}.txt")
            
            with open(content_path, "r") as f:
                expected = f.read().rstrip()
            with open(result_path, "r") as f:
                result = f.read().rstrip()
            
            try:
                self.assertMultiLineEqual(expected, result, f"Test {i+1} failed")
            except AssertionError as e:
                print(f"\033[91mScenario 6 Case {i+1}: FAILURE\033[0m")
                raise e
            else:
                print(f"\033[92mScenario 6 Case {i+1}: SUCCESS\033[0m")
    
    def test_07(self):
        print("\n")
        for i in range(3):
            self.make_run(7, i + 1)
            
            content_path = os.path.join(project_root, f"cases/tests/scenar_7/output{i+1}.txt")
            result_path = os.path.join(project_root, f"cases/local/output7.{i+1}.txt")
            
            with open(content_path, "r") as f:
                expected = f.read().rstrip()
            with open(result_path, "r") as f:
                result = f.read().rstrip()
            
            try:
                self.assertMultiLineEqual(expected, result, f"Test {i+1} failed")
            except AssertionError as e:
                print(f"\033[91mScenario 7 Case {i+1}: FAILURE\033[0m")
                raise e
            else:
                print(f"\033[92mScenario 7 Case {i+1}: SUCCESS\033[0m")


if __name__ == '__main__':
    unittest.main()
