from yaku.scheduler \
    import \
        run_tasks
from yaku.context \
    import \
        get_bld, get_cfg

def configure(ctx):
    ctx.use_tools(["ctasks", "cxxtasks"])
    ctx.env.append("DEFINES", "_FOO")

    cc = ctx.builders["ctasks"]
    assert cc.try_compile("foo", "int main() {}")
    assert not cc.try_compile("foo", "intt main() {}")

if __name__ == "__main__":
    ctx = get_cfg()
    configure(ctx)
    ctx.store()