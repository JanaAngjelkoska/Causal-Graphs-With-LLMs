import networkx as nx
import matplotlib.pyplot as plt

class Builder:
    def build_graph(self, graph):
        """
        Build and visualize a graph from edges and variables sent after the pipeline finishes.

        Args:
            graph (dict): Dictionary where keys are variables and values are lists of caused variables.

        Returns:
            None: Displays the graph visualization.
        """
        G = nx.DiGraph()

        for source, targets in graph.items():
            for target in targets:
                G.add_edge(source, target)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000,
                font_size=10, font_weight='bold', arrows=True, edge_color='gray')

        plt.title("Causal Graph")
        plt.axis('off')
        plt.savefig("causal_graph.png")
        logger = None
        try:
            import logging
            logger = logging.getLogger(__name__)
        except ImportError:
            pass
        if logger:
            logger.info("Causal graph saved to causal_graph.png")
        import sys
        if hasattr(sys, 'ps1') or sys.flags.interactive:
            plt.show()
        else:
            plt.close()
