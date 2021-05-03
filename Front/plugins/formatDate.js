export default ({ app }, inject) => {
    inject('formatDate', value => {
        if (value) {
            const date = new Date(value);
            const day = date.getDate();
            const month = date.getMonth();
            const year = date.getFullYear();

            return `${day}/${month + 1}/${year}`;
        }
    })
}