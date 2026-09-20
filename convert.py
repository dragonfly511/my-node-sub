import base64

INPUT_FILE = "nodes.txt"
OUTPUT_FILE = "subscription.txt"


def main():
    nodes = []

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            nodes.append(line)

    content = "\n".join(nodes)

    encoded = base64.b64encode(
        content.encode("utf-8")
    ).decode("utf-8")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(encoded)

    print("转换完成")
    print("节点数量:", len(nodes))
    print("输出文件:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
