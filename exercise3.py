# sliding window technique: 
# - if i use two pointers, then you don't have to use anohter array to measure the length => saves space complexity 
# - if you add another condition that the index of the char in the dict must be greater than the start-pointer to be evaluated as already-seen, then it works out
# ==> in fact, you don't even need an end pointer, as the index(i) is always the end
def lengthOfLongestSubstringWithEndVar(input:str):
    seen:dict = {}
    start: int = 0
    end: int = 0
    tracker:int = 0
    # do i need another variable to track the length of the longest substring?
    for (i,char) in enumerate(input):
        if char in seen:
            if seen[char] >= start:
                if (end-start) > tracker: tracker= (end-start) 
                start = seen[char] + 1
        # automatically updates?
        seen[char] =i
        end += 1
    if (end-start) > tracker: tracker= (end-start) 
    return tracker
    
def lengthOfLongestSubstringWithoutEndVarAndCalculatesMaxEveryIteration(input: str):
    seen:dict = {}
    start: int = 0
    tracker:int = 0
    # do i need another variable to track the length of the longest substring?
    for (i,char) in enumerate(input):
        if char in seen and seen[char] >= start: 
            start = seen[char] + 1
        # automatically updates?
        seen[char] =i
        # calculating the max every iteration is not efficient, as this results in more operations 
        tracker = max(tracker, i - start+1) 
    return tracker

                

                




# method that uses a set to track all the seen characters, then deleting the characters before the matching char through iteration => O(n^2) worst case
 
def lengthOfLongestSubstring2(input: str):
    chars:set = set()
    tracker:str = ""
    len_tracker:int = 0

    for char in input:
        print("tracker:",tracker, "current char:", char, "set:", chars)
        if char in chars:
            # update the longest length 
            if len(tracker) > len_tracker: len_tracker = len(tracker)
            # remove characters before the same character from the set
            for (i,l) in enumerate(tracker):
                chars.remove(l)
                print("after removed:",chars)
                if l == char: 
                    tracker = tracker[i+1:]
                    break
        # add the current char to the set and the tracker
        chars.add(char)
        tracker += char
    # the last unchecked part of the string
    if len(tracker) > len_tracker: return len(tracker)
    return len_tracker

# Releastically, this leads to an O(26n) time complexity on average, as there are only 26 characters, but in the case where  
            

def lengthOfLongestSubstring3(input:str):
    chars:dict = {}
    tracker:str = ""
    len_tracker:int = 0

    for (i,char) in enumerate(input):
        if char in chars:
            if len(tracker) > len_tracker: len_tracker = len(tracker)
            for l in tracker:
                chars.pop(l)

            if char != tracker[0]: 
                print("tracker before opeartion:", tracker[:chars.get(char)-1],chars.get(char))
                print(tracker)
                for c in tracker[:chars.get(char) - 1]:
                    print("popped!", c)
                    chars.pop(c)
            print(chars)
            tracker = tracker[chars.get(char) + 1:]
            print("same char found:", char, " tracker: ", tracker)
        chars[char] = i
        tracker += char
        print(tracker)
    if len(tracker) > len_tracker: return len(tracker)
    return len_tracker

input:str= "dvdf"
print(lengthOfLongestSubstring(input))

