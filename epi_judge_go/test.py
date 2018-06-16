import sys
import subprocess

test_dir = '../test_data'

if __name__ == "__main__":
    name = sys.argv[1]
    print(name)
    test_file = "../test_data/{}.tsv".format(name)
    with open(test_file, 'r') as tf:
        tests = tf.readlines()
    c = 1
    len_t = len(tests)
    for t in tests[1:]:
        t = t.split('\t')
        test_input = t[0]
        #print(len(t))
        test_cmd = [ "./{}".format(name), test_input]
        #print(" ".join(test_cmd))
        test_output = subprocess.run(test_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8').replace('\n','')
        check = t[1]
        #print(test_input, test_output, check)
        if check != test_output:
            print("FAILED TEST!")
            print(check, test_output)
            sys.exit()

        print("[{}\t/{} tests passed]".format(c,len_t), end = "\r")
        c+=1
    print("[{}\t/{} tests passed]".format(c,len_t))
    
