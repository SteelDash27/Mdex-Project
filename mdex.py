import argparse
from src.scanner import load_config, scan_markdown_files

def main():
    parser = argparse.ArgumentParser(prog = "mdex")
    subparser = parser.add_subparsers(dest = "command")

    #Defining Mdex subcommands
    scan_parser = subparser.add_parser("scan")
    scan_parser.add_argument("--root", help = "Tell the machine to scan markdown files in a specific user-defined directory.")
    scan_parser.add_argument("--dry-run", action = "store_true", help = "Give user a preview of a certain command without executing it.")

    #Actually parsing cli arguments
    args = parser.parse_args()

    if args.command == "scan":
        config = load_config()
       #If the user didnt use the --root subcommand then use the roots stored in our config file 
        roots = [args.root] if args.root else config["roots"]
        files = scan_markdown_files(roots,config["ignore_dirs"])

        if args.dry_run:
            for f in files:
                #This just shows us all the files that the scan_markdown_files function found
                print(f)
        else:
            print(f"Found {len(files)} files (indexing not implemented yet.)")

if __name__ == "__main__":
    main()
