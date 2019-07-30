addlink() {
    local root=~/dev/github/links

    "$root/.virtualenv/bin/python" "$root/links.py" --add "$@" && make -C "$root"
}
