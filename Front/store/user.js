import {
  set
} from "@/utils/actions"

export const state = () => {
  return {
    api: {
      api: 'http://127.0.0.1:8080/api',
    },
    user_info: {},
    dataUpdate: {},
    list_user_info: [],
    list_admin_info: [],
    dataRegister: {},
    dataChangePass: {},
  }
}

export const mutations = {
  GET_USER_BY_ID: set('user_info'),

  UPDATE_USER: set('dataUpdate'),

  CHANGE_PASSWORD_USER: set('dataChangePass'),

  LIST_USER_INFO: set('list_user_info'),

  LIST_ADMIN_INFO: set('list_admin_info'),

  REGISTER: set('dataRegister')

}

export const actions = {

  async getUserById({ state, commit }, id) {
    const { api } = state.api
    const res = { isSuccess: false }
    const token = this.$auth.$storage.getUniversal('token')
    this.$axios.setHeader('Authorization', "Bearer " + token)

    try {

      const data = await this.$axios.$post(`${api}/info`, id)
      commit('GET_USER_BY_ID', data)
      res.isSuccess = true
    }
    catch (err) {
      console.log(err)
    }
    return res
  },

  async changePasswordUser({ state, commit }, dataReq) {
    const { api } = state.api
    const res = { isSuccess: false }
    const token = this.$auth.$storage.getUniversal('token')
    this.$axios.setHeader('Authorization', "Bearer " + token)

    try {

      const data = await this.$axios.$post(`${api}/change-password`, dataReq)
      commit('CHANGE_PASSWORD_USER', data)
      res.isSuccess = true
    }
    catch (err) {
      console.log(err)
    }
    return res
  },

  async updateInfoUser({ state, commit }, dataReq) {
    const { api } = state.api
    const res = { isSuccess: false }
    const token = this.$auth.$storage.getUniversal('token')
    this.$axios.setHeader('Authorization', "Bearer " + token)

    try {

      const data = await this.$axios.$put(`${api}/user-info/${dataReq.id}`, dataReq)
      commit('UPDATE_USER', data)
      res.isSuccess = true
    }
    catch (err) {
      console.log(err)
    }
    return res
  },

  async getListUsers({ state, commit }) {
    const { api } = state.api
    const res = { isSuccess: false }
    const token = this.$auth.$storage.getUniversal('token')
    this.$axios.setHeader('Authorization', "Bearer " + token)

    try {

      const data = await this.$axios.$post(`${api}/list-user`)
      commit('LIST_USER_INFO', data)
      res.isSuccess = true
    }
    catch (err) {
      console.log(err)
    }
    return res
  },

  async getListAdmin({ state, commit }) {
    const { api } = state.api
    const res = { isSuccess: false }
    const token = this.$auth.$storage.getUniversal('token')
    this.$axios.setHeader('Authorization', "Bearer " + token)

    try {

      const data = await this.$axios.$post(`${api}/list-admin`)
      commit('LIST_ADMIN_INFO', data)
      res.isSuccess = true
    }
    catch (err) {
      console.log(err)
    }
    return res
  },

  async registerUA({ state, commit }, dataReq) {
    const { api } = state.api
    const res = { isSuccess: false }

    try {

      const data = await this.$axios.$post(`${api}/register`, dataReq)
      commit('REGISTER', data)
      res.isSuccess = true
    }
    catch (err) {
      console.log(err)
    }
    return res
  },

}