def sum_appearances(file_name):
    d = {}
    with open(file_name) as f:
        # read line by line
        for line in f:
            # now read each character:
            for c in line:
                # c is each character now
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
        #at this point the dictionary is complete
        # sort out the values to get the 2 most common ones
        print(d)
        values = list(d.values())
        values.sort(reverse=True)
        return values[0] + values[1]

print(sum_appearances("hp.txt"))