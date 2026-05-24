import matplotlib.pyplot as plt
import numpy as np

def generate_chart():
    labels = ["Actual MTD", "Finpro", "Budget", "LY"]

    values = [
        187585159,
        136331217,
        129215900,
        116508667
    ]

    expected_mtd = 131607134

    colors = [
        "#8FC646",
        "#144800",
        "#60AA3E",
        "#C2F281"
    ]

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(labels))

    bars = ax.bar(
        x,
        values,
        width=0.58,
        color=colors,
        zorder=2
    )

    # Expected MTD line
    ax.axhline(
        y=expected_mtd,
        color="#3D4F3D",
        linestyle="--",
        linewidth=2.5,
        zorder=5
    )

    ax.text(
        1.5,
        expected_mtd + 4000000,
        "Expected MTD ($131,607,134)",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
        color="#2E3B2E"
    )

    # Bar labels
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value / 2,
            f"${value:,.0f}",
            ha="center",
            va="center",
            rotation=90,
            fontsize=10,
            fontweight="bold",
            color="white"
        )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11, fontweight="bold")

    ax.yaxis.set_visible(False)

    for spine in ["top", "left", "right"]:
        ax.spines[spine].set_visible(False)

    ax.spines["bottom"].set_color("#CCCCCC")

    plt.title(
        "Total Company Sales MTD",
        fontsize=16,
        fontweight="bold"
    )

    plt.tight_layout()

    # ✅ GitHub Actions friendly output (NO /tmp path)
    output_file = "mtd_chart.png"
    plt.savefig(output_file, bbox_inches="tight", dpi=200)

    plt.close(fig)

    print(f"Chart generated: {output_file}")


if __name__ == "__main__":
    generate_chart()