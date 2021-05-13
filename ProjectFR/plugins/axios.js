export default function ({ app, $axios, redirect }) {
    $axios.onError(error => {
        const code = parseInt(error.response && error.response.status)
        if (code === 403 || code === 401) {
            app.$auth.$storage.removeUniversal('user')
            redirect('/login')
        }
    })
}
