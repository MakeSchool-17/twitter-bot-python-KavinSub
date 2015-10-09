import sys
import collections
import hashtable_6
import tokenizer
import random
# N tokens per state
N = 0
filename = ""
regex = "'[\w'.]*',|]"

# Given a linked list, formatted (next_token, count) return a list with (next_token, probability)
def calculate_probabilities(linkedlist):
    pairs = linkedlist.get_values()
    # New list
    newlist = hashtable_6.LinkedList()
    total = 0
    # Calculate total number of tokens
    for pair in pairs:
        total += pair[1]
    # Now calculate probability of each token where P(token) = token_occurences / total
    # Then add the total probability of all previous elements
    total_prob = 0.0
    for pair in pairs:
        this_prob = float(pair[1]) / float(total)
        total_prob += this_prob
        newlist.append(hashtable_6.Node(pair[0], this_prob + total_prob))
    return newlist

# Returns a grammar string representation of the deque object
def deque_str(deque):
    deque_copy = deque.copy()
    deq_str = ""
    for i in range(len(deque_copy)):
        deq_str += "{} ".format(deque_copy.popleft())
    deq_str = deq_str.strip()
    return deq_str

def create_map(tokens, N):
    # Hashtable used to store everything
    hashtable = hashtable_6.HashTable(500)
    # Queue to iterate through words
    queue = collections.deque()
    #print(tokens)
    # Initalize first state
    for i in range(N):
        queue.append(tokens[i])
    prev = deque_str(queue)
    # Initialize initial state of markov chain
    begin_state = prev
    # Iterate through all tokens
    for i in range(N, len(tokens)):
        queue.popleft()
        queue.append(tokens[i])
        curr = deque_str(queue)
        if hashtable.contains(prev) is False:
            hashtable.set(prev, hashtable_6.LinkedList())
        linkedlist = hashtable.get(prev)
        node = linkedlist.find(lambda k: curr == k)
        if node is not None:
             node.data += 1
        else:
            linkedlist.append(hashtable_6.Node(curr, 1))
        prev = curr
    # Calculate probabilities
    pairs = hashtable.get_pairs()
    for pair in pairs:
        newlist = calculate_probabilities(pair[1])
        hashtable.update(pair[0], newlist)
    # Now the hashtable is our final markov chain
    return (hashtable, begin_state)

# Prints a k token sequence based on the markov chain
def generate_sequence(markovchain, begin_state, k):
    curr_state = ""
    # If begin state has not been specified, pick a random word
    if begin_state is None:
        pairs = markovchain.get_pairs()
        curr_state = pairs[random.randint(0, len(pairs) - 1)][0]
    else:
        curr_state = begin_state
    words = curr_state.split()
    sequence = "{} ".format(words[0].title())
    next_state = ""
    lower_bound = 0.0
    # Boolean to signify end of generation
    end = False
    l = 0
    while True:
        state_list = markovchain.get(curr_state)
        # If no state list is available, we end our generation
        if state_list is None or end is True:
            final_tokens = curr_state.split()
            final_token = ""
            for j in range(1, len(final_tokens)):
                final_token += "{} ".format(final_tokens[j])
            sequence += "{} ".format(final_token)
            break
        # Begin iteration through the list to find a value within range [lower_bound, curr_data]
        rand_num = random.uniform(0, 1)
        curr_node = state_list.head
        while curr_node != None:
            # If rand_num falls in the designated probability range, that is our next state
            if rand_num >= lower_bound and rand_num <= curr_node.data:
                next_state = curr_node.key
                break
            #lower_bound += curr_node.data
            curr_node = curr_node.next
        # Add the next word to the sequence
        sequence += "{} ".format(next_state.split()[0])
        curr_state = next_state
        lower_bound = 0.0
        l += 1
        # Ensures the sentence generated ends appropriately
        if l >= k and next_state[len(next_state) - 1] is '.':
            end = True
    return sequence
if __name__ == '__main__':
    # Command line args conditionals
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        N = int(sys.argv[2])
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        N = 1
    else:
        filename = "markov_test_1.txt"
        N = 1
    begin_state = ""
    directory = "text_files/" + filename
    # Deque object used to store n-token states
    tokens = tokenizer.tokenizer(directory)
    markovchain, begin_state = create_map(tokens, N)
    #pairs = markovchain.get_pairs()
    #for i in range(50):
        #print("{} contains {}".format(pairs[i][0], pairs[i][1]))
    generated_string = generate_sequence(markovchain, None, 25)
    print(generated_string)
