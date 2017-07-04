from belgium_exo import cli, feature


def main():
    args = cli.parse_args()
    item = feature.load(args.src_path, args.iso_code)
    feature.append(args.dst_path, item)


if __name__ == '__main__':
    main()
