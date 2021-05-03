<template>
  <div class="bg-grey-lighter min-h-screen flex flex-col">
    <br />
    <div
      class="container max-w-sm mx-auto flex-1 flex flex-col items-center justify-center px-2"
    >
      <div class="bg-white px-6 py-8 rounded shadow-md text-black w-full">
        <h1 class="mb-8 text-3xl text-center">Đăng kí tài khoản</h1>

        <div class="flex flex-wrap -mx-3 mb-2">
          <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
              id="grid-first-name"
              type="text"
              placeholder="Họ"
              v-model.trim="userInfo.first_name"
            />
          </div>
          <div class="w-full md:w-1/2 px-3">
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              id="grid-last-name"
              type="text"
              placeholder="Tên"
              v-model.trim="userInfo.last_name"
            />
          </div>
          <!-- <div class="w-full mt-2 px-3 mb-1 md:mb-0">
            <div class="relative">
              <select
                class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                id="grid-state"
                placeholder="Gender"
                v-model="userInfo.gender"
              >
                <option value="0">Nam</option>
                <option value="1">Nữ</option>
                <option value="2">Khác</option>
              </select>
              <div
                class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
              >
                <svg
                  class="fill-current h-4 w-4"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                  />
                </svg>
              </div>
            </div>
          </div> -->
        </div>
        <div class="flex flex-wrap -mx-3 mb-6">
          <div class="w-full px-3">
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              id="grid-username"
              type="text"
              placeholder="Số điện thoại"
              v-model="userInfo.phone"
            />
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              id="grid-username"
              type="text"
              placeholder="Địa chỉ"
              v-model="userInfo.live_at"
            />
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              id="grid-email"
              type="text"
              placeholder="*Email"
              v-model="userInfo.email"
              required
            />
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              id="grid-password"
              type="password"
              placeholder="*Mật khẩu"
              v-model="userInfo.password"
              required
            />
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              id="grid-repassword"
              type="password"
              placeholder="*Xác nhận mật khẩu"
              v-model="rePassword"
              required
            />
          </div>
        </div>
        <button
          @click="registerU"
          class="w-full bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded-full"
        >
          Tạo tài khoản
        </button>
      </div>
      <div>
        <br />
        <p class="text-center text-sm text-gray-600 font-thin">
          Nếu bạn đã có tài khoản?
          <a
            v-on:click="loginInfoUser"
            class="text-blue-500 no-underline hover:underline"
            >Đăng nhập</a
          >
        </p>
      </div>
      <br />
    </div>
  </div>
</template>

<script>
import validations from "../utils/validations";
import { mapState, mapActions } from "vuex";
export default {
  layout: "begin",
  data() {
    return {
      userInfo: {
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        phone: "",
        live_at: "",
      },
      rePassword: "",
      dataRegister: {},
    };
  },
  computed: {
    ...mapState("user", ["dataregister"]),
    checkPass() {
      if (this.userInfo.password === this.rePassword) return true;
      else return false;
    },
  },
  methods: {
    ...mapActions("user", ["registerUA"]),

    loginInfoUser() {
      setTimeout(() => {
        this.$router.push("/");
      }, 500);
    },

    async registerU() {
      if (this.checkPass) {
        const { isSuccess } = this.registerUA(this.userInfo);
        if (isSuccess) {
          if (this.dataRegister.statusCode === 200) {
            setTimeout(() => {
              this.$router.push("/");
            }, 500);
          } else {
            this.$buefy.dialog.alert({
              title: "Error",
              message: "Đăng ký không thành công!",
              type: "is-danger",
              hasIcon: true,
              icon: "times-circle",
              iconPack: "fa",
              ariaRole: "alertdialog",
              ariaModal: true,
            });
          }
        }
      } else {
        this.$buefy.dialog.alert({
          title: "Error",
          message: "Làm ơn xác nhận lại mật khẩu!",
          type: "is-danger",
          hasIcon: true,
          icon: "times-circle",
          iconPack: "fa",
          ariaRole: "alertdialog",
          ariaModal: true,
        });
      }
    },
  },
};
</script>
