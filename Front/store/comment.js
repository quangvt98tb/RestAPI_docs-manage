import {
    set
} from "@/utils/actions"

export const state = () => {
    return {
        api: {
            api: 'http://127.0.0.1:8080/api'
        },
        dataCreateComment: {},
        dataUpdateComment: {},
        dataDeleteComment: {},
        list_comment: []
    }
}

export const mutations = {
    CREATE_COMMENT: set('dataCreateComment'),

    UPDATE_COMMENT: set('dataUpdateComment'),

    DELETE_COMMENT: set('dataDeleteComment'),

    GET_LIST_COMMENT: set('list_comment')
}


export const actions = {

    async listComment({ state, commit }, id_doc) {

        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$post(`${api}/list-comment`, id_doc)

            commit('GET_LIST_COMMENT', data)
            res.isSuccess = true
        } catch (err) {
            console.log('list comment', err)
        }
        return res
    },

    async createComment(
        { state, commit },
        dataReq
    ) {
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$post(`${api}/comment`, dataReq)

            commit('CREATE_COMMENT', data)
            res.isSuccess = true
        } catch (err) {
            console.log('create comment', err)
        }
        return res
    },

    async updateComment(
        { state, commit },
        dataReq
    ) {
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$put(`${api}/comment/${dataReq.id}`, dataReq)

            commit('UPDATE_COMMENT', data)
            res.isSuccess = true
        } catch (err) {
            console.log('update comment', err)
        }
        return res
    },

    async deleteComment(
        { state, commit },
        dataReq
    ) {
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$delete(`${api}/comment/${dataReq.id}`, dataReq)

            commit('DELETE_COMMENT', data)
            res.isSuccess = true
        } catch (err) {
            console.log('delete comment', err)
        }
        return res
    },
}