import os
import json
from pathlib import Path
import glob
from grader_output import GraderOutput
from runners import RUNNERS
import traceback

if __name__ == "__main__":
    try:
        # Step one: load the tests
        with open("./tests.json") as tests_file:
            tests = json.loads(tests_file.read())
        # Step two: identify the type of the file
        for ext in GraderOutput.VALID_EXT:
            if ext != "java":
                file_path = Path(f"input.{ext}")
                if file_path.exists():
                    break
            else:
                # Java is a special case as it won't be named "input.java"
                # so we have to look for ".java" files.
                pattern = r"./*java"
                files = glob.glob(pattern)
                if len(files) != 1:
                    continue
                file_path = Path(files[0])
                break
        # Step three: chose the apropriate runner
        runner = RUNNERS[ext]
        # Step four: run the tests
        results = []
        raised = False
        for input_str in tests.keys():
            code, output = runner(str(file_path), input_str)
            if code != 0:
                raised = True
            results.append(output)
        # Step five: create the GraderOutput object
        retval = GraderOutput({
            "submission_id": os.getenv("SUBMISSION") or -1,
            "tests": tests,
            "status": "F" if not raised else "E", # TODO: Store this somewhere?
            "results": results
        })
        # Step six: print it
        #print("printing")
        print(retval.serialize())
        #print()
    except Exception as e:
        # Print the error message and the stack trace
        print(f"Error: {str(e)}")
        print(traceback.format_exc())