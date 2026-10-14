"""Build checkpoint_skeleton.pdf: 3 letter-landscape pages.

Page 1: Viz A + Viz A2 (both "it's real" charts).
Page 2: Viz B + placeholder for the second "it's overstated" chart.
Page 3: proposition and deceptive-technique bullets.
"""
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle

ROOT = Path(__file__).parent
INK_2 = "#52514e"

plt.rcParams["font.family"] = ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"]


def chart_page(pdf, heading, image, second=None, placeholder=None):
    """Two charts stacked on one page; `second` is an image file, or `placeholder` text if not built yet."""
    fig = plt.figure(figsize=(11, 8.5))
    fig.text(0.05, 0.955, heading, fontsize=16, fontweight="bold")
    ax = fig.add_axes([0.05, 0.47, 0.9, 0.46])
    ax.imshow(mpimg.imread(ROOT / image))
    ax.set_axis_off()
    box = fig.add_axes([0.05, 0.04, 0.9, 0.39])
    box.set_axis_off()
    if second:
        box.imshow(mpimg.imread(ROOT / second))
    else:
        box.add_patch(Rectangle((0, 0), 1, 1, fill=False, ls="--", ec=INK_2, transform=box.transAxes))
        box.text(0.5, 0.5, placeholder, ha="center", va="center", fontsize=13, color=INK_2,
                 transform=box.transAxes)
    pdf.savefig(fig)
    plt.close(fig)


with PdfPages(ROOT / "checkpoint_skeleton.pdf") as pdf:
    chart_page(pdf, "Side 1: Climate change is real", "viz_A_choropleth.png",
               second="viz_A2_share_warmer.png")
    chart_page(pdf, "Side 2: Climate change is overstated", "viz_B_yoy.png",
               placeholder="[ Second \"it's overstated\" visualization goes here ]")

    md = (ROOT / "design_decisions.md").read_text()
    bullets = md.split("## Checkpoint page 3: deceptive techniques (bullets)")[1].strip()
    bullets = bullets.replace("**", "").replace("*", "")
    fig = plt.figure(figsize=(11, 8.5))
    fig.text(0.06, 0.94, "Proposition and deceptive techniques", fontsize=16, fontweight="bold")
    fig.text(0.06, 0.89, bullets, fontsize=11.5, va="top", wrap=True, linespacing=1.5)
    pdf.savefig(fig)
    plt.close(fig)

print("saved checkpoint_skeleton.pdf")
