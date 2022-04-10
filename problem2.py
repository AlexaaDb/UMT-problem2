# Function to find the number of possible rectangles
def numberRectangles(ob):
    # We create TreeSet containing elements
    ts = set()

    # We insert the pairs in the set
    for i in range(len(sample)):
        ts.add(f"{sample[i]}");

    ans = 0;
    for i in range(len(sample)):
        for j in range(len(sample)):
            if (sample[i][0] != sample[j][0] and sample[i][1] != sample[j][1]):

                # Searching the pairs in the set
                if (f"{[sample[i][0], sample[j][1]]}" in ts and f"{[sample[j][0], sample[i][1]]}" in ts):
                    # Increase the answer
                    ans += 1

    # Return the final answer
    # the final answer represents the result of the division by 4 of all the sides that we found
    return int(ans / 4);

if __name__=="__main__":
    # sample input 1
    # N=number of points in the sample input
    N = 6;
    sample = [0] * N
    sample[0] = [1, 1];
    sample[1] = [1, 3];
    sample[2] = [2, 1];
    sample[3] = [2, 3];
    sample[4] = [3, 1];
    sample[5] = [3, 3];

    print(" The first sample output: ", numberRectangles(sample));

    # sample input 2
    # N=number of points in the sample input
    N = 5;
    sample = [0] * N
    sample[0] = [1, 1];
    sample[1] = [1, 3];
    sample[2] = [2, 3];
    sample[3] = [3, 1];
    sample[4] = [3, 3];

    print(" The second sample output: ", numberRectangles(sample));