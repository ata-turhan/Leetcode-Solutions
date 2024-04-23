from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        total_node_count = n
        
        if total_node_count == 1:
            # Quick response for one node tree
            return [0]
        
        
        # build adjacency matrix
        adj_matrix = defaultdict( set )
        
        for src_node, dst_node in edges:
            adj_matrix[src_node].add( dst_node )
            adj_matrix[dst_node].add( src_node )
            
            
        # get leaves node whose degree is 1
        leave_nodes = [ node for node in adj_matrix if len(adj_matrix[node]) == 1 ]
        
        
        # keep doing leave nodes removal until total node count is smaller or equal to 2
        while total_node_count > 2:
            
            total_node_count -= len(leave_nodes)
            
            leave_nodes_next_round = []
            
            # leave nodes removal
            for leaf in leave_nodes:
                
                neighbor = adj_matrix[leaf].pop()
                adj_matrix[neighbor].remove( leaf )
                
                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append( neighbor )
                    
            leave_nodes = leave_nodes_next_round
        
        # final leave nodes are root node of minimum height trees
        return leave_nodes
                