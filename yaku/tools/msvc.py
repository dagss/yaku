def detect(ctx):
    env = ctx.env

    ctx.env["CC"] = ["cl.exe"]
    ctx.env["CC_TGT_F"] = ["/c", "/Fo"]
    ctx.env["CC_SRC_F"] = []
    ctx.env["CFLAGS"] = []
    ctx.env["CPPPATH"] = []
    ctx.env["CPPPATH_FMT"] = "/I%s"
    ctx.env["LINK"] = ["link.exe"]
    ctx.env["LINKFLAGS"] = []
    ctx.env["LIBS"] = []
    ctx.env["LIB_FMT"] = "%s.lib"
    ctx.env["LIBDIR"] = []
    ctx.env["LIBDIR_FMT"] = "/L%s"