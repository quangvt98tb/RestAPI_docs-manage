import {
    set
} from "@/utils/actions"

export const state = () => {
    return {
        api: {
            api: 'http://127.0.0.1:8080/api',
            api_correct: 'http://localhost:8890/api'
        },
        dataDocs: [],
        dataCreateDoc: {},
        doc: {},
        dataShare: {},
        listShareFix: [],
        listShareRead: [],
        dataUpdateDoc: {},
        dataDeleteDoc: {},
        listdocsdel: [],
        dataCorrect: {},
        delData: {},
        dataRestore: {}
    }
}

export const mutations = {
    CHECK_CORRECT_DOC: set('dataCorrect'),

    LIST_DOC_BY_ID_USER: set('dataDocs'),

    LIST_DOCS_SHARE_FIX: set('listShareFix'),

    LIST_DOCS_SHARE_READ: set('listShareRead'),

    SHARE_DOC: set('dataShare'),

    RESTORE_DOCS: set('dataRestore'),

    CREATE_DOC: set('dataCreateDoc'),

    UPDATE_DOC: set('dataUpdateDoc'),

    DELETE_DOC: set('dataDeleteDoc'),

    DELETE_VV_DOC: set('delData'),

    GET_DOC_BY_ID: set('doc'),

    GET_LIST_DOCS_DELETED: set('listdocsdel')
}


export const actions = {

    async checkCorrectDoc({ state, commit }, dataReq) {
        const res = { isSuccess: false }
        const { api } = state.api_correct
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {
            const data = await this.$axios.$post(`${api}/spell`, dataReq)
            commit('CHECK_CORRECT_DOC', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async shareDoc({ state, commit }, dataReq) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {

            const data = await this.$axios.$post(`${api}/share-doc`, dataReq)
            commit('SHARE_DOC', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async getListDocsShareFix({ state, commit }, id) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {

            const data = await this.$axios.$post(`${api}/list-share-fix-docs`, id)
            commit('LIST_DOCS_SHARE_FIX', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async getListDocsShareRead({ state, commit }, id) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {

            const data = await this.$axios.$post(`${api}/list-share-read-docs`, id)
            commit('LIST_DOCS_SHARE_READ', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async getListDocsById({ state, commit }, id) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {

            const data = await this.$axios.$post(`${api}/list-docs`, id)
            commit('LIST_DOC_BY_ID_USER', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async getListDeleteDocsById({ state, commit }, id) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {

            const data = await this.$axios.$post(`${api}/delete-docs`, id)
            commit('GET_LIST_DOCS_DELETED', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async deleteDoc({ state, commit }, id) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {
            const data = await this.$axios.$post(`${api}/delete-doc`, id)
            commit('DELETE_DOC', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async restoreDocs({ state, commit }, ids) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {
            const data = await this.$axios.$post(`${api}/restore-docs`, ids)
            commit('RESTORE_DOCS', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async getDocsById({ state, commit }, id) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {

            const data = await this.$axios.$post(`${api}/doc-detail`, id)
            commit('GET_DOC_BY_ID', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async createDocument({ state, commit }, dataReq) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {
            const data = await this.$axios.$post(`${api}/docs`, dataReq)
            commit('CREATE_DOC', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async updateDocument({ state, commit }, dataReq) {
        const { api } = state.api
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        try {
            const data = await this.$axios.$put(`${api}/docs/${dataReq.id}`, dataReq)
            commit('UPDATE_DOC', data)
            res.isSuccess = true
        }
        catch (err) {
            console.log(err)
        }
        return res
    },

    async deleteDocVV(
        { state, commit },
        dataReq
    ) {
        const res = { isSuccess: false }
        const token = this.$auth.$storage.getUniversal('token')
        this.$axios.setHeader('Authorization', "Bearer " + token)

        const { api } = state.api

        try {
            const data = await this.$axios.$post(`${api}/docs-del`, dataReq)

            commit('DELETE_VV_DOC', data)
            res.isSuccess = true
        } catch (err) {
            console.log('delete doc', err)
        }
        return res
    },
}
