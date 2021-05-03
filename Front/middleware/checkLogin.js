export default function (ctx) {
    const user = ctx.$auth.user
    if (!user) {
        ctx.redirect('/login')
    }
}
