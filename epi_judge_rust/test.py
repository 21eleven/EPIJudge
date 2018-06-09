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
        #print(len(t))
        if len(t) == 3:
            test_input = [t[0]]
            check = t[1]
        if len(t) == 4:
            test_input = t[0:2]
            check = t[2]
        if len(t) == 5:
            test_input = t[0:3]
            check = t[3]
        test_cmd = [ "./{}".format(name)] + test_input
        #print(" ".join(test_cmd))
        test_output = subprocess.run(test_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8').replace('\n','')
        #print(test_input, test_output, check)
        if check != test_output:
            print("FAILED TEST!")
            print(check, test_output)
            sys.exit()

        print("[{}\t/{} tests passed]".format(c,len_t), end = "\r")
        c+=1
    print("[{}\t/{} tests passed]".format(c,len_t))
    
