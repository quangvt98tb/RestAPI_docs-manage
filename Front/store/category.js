import {
    set
} from "@/utils/actions"

export const state = () => {
    return {
        api: {
            api: 'http://127.0.0.1:8080/api'
        },
        dataCreateCategory: {},
        dataUpdateCategory: {},
        dataDeleteCategory: {},
        list_category: []
    }
}

export const mutations = {
    CREATE_CATEGORY: set('dataCreateCategory'),

    UPDATE_CATEGORY: set('dataUpdateCategory'),

    DELETE_CATEGORY: set('dataDeleteCategory'),

    GET_LIST_CATEGORY: set('list_category')
}


export const actions = {

    async listCategory({ state, commit }) {

        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$get(`${api}/category`)

            commit('GET_LIST_CATEGORY', data)
            res.isSuccess = true
        } catch (err) {
            console.log('list category', err)
        }
        return res
    },

    async createCategory(
        { state, commit },
        dataReq
    ) {
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$post(`${api}/category`, dataReq)

            commit('CREATE_CATEGORY', data)
            res.isSuccess = true
        } catch (err) {
            console.log('create category', err)
        }
        return res
    },

    async updateCategory(
        { state, commit },
        dataReq
    ) {
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$put(`${api}/category/${dataReq.id}`, dataReq)

            commit('UPDATE_CATEGORY', data)
            res.isSuccess = true
        } catch (err) {
            console.log('update category', err)
        }
        return res
    },

    async deleteCategory(
        { state, commit },
        dataReq
    ) {
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$delete(`${api}/category/${dataReq.id}`, dataReq)

            commit('DELETE_CATEGORY', data)
            res.isSuccess = true
        } catch (err) {
            console.log('delete category', err)
        }
        return res
    },
}