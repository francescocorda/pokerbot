from tree_elements.terminal_node import TerminalNode

def in_chars(string):
    return [char for char in string]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def visualize(el, level):
    if el.children is not None:
        for key, value in el.children.items():
            print('{:<15}'.format(value.history[-1] + '  ->'), end='')
            visualize(value, level+1)
            player = 1
            if isinstance(value, TerminalNode):
                for payoff in value.payoffs:
                    print('{:^10}'.format(bcolors.HEADER + bcolors.BOLD + '(' + str(player) + '=' + str(payoff) + ')' + bcolors.ENDC), end=' ')
                    player = 2
            num = 0
            print('')
            while num < level:
                print('{:>15}'.format(' |'), end='')
                num += 1
    else:
        return


def clustering_table_creation(root):
    # dictionary indexed by action and utility that stores every node that can return that utility
    cluster_table = {}
    # cycle through each children of the root, saves the list of nodes for the utlities of that action
    for node in root.children.items():
        for action in node.actions:
            if node.player == '1':
                cluster_table[action, node.children['P' + node.player + ':' + action].compute_utilities()[0]]\
                    .append(node.history[-1])
            if node.player == '2':
                cluster_table[action, node.children['P' + node.player + ':' + action].compute_utilities()[1]]\
                    .append(node.history[-1])

    # old code to reverse the dictionary
    # for node, action, utility in cluster_table.items():
    #     cluster_table[action, utility] = search_node(cluster_table, action, utility)


# old code used to reverse the dictionary used to build the cluster table
def search_node(dictionary, action, utility):
    nodes_list = []
    for index_node, index_action, index_utility in dictionary.items():
        if dictionary[index_node, index_action] == utility:
            nodes_list.append(index_node)
    return nodes_list
