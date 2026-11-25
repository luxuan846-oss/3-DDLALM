"""Draw the IllCondL1 r6 metrics from this experiment's results directory."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from plot_r6_metrics import main


if __name__ == "__main__":
    main("ill")
