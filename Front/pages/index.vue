<template>
  <div class="bg-grey-100">
    <div class="min-h-screen w-full p-6 flex justify-center items-center">
      <div class="w-full max-w-xs">
        <div class="bg-white border p-8 shadow rounded w-full mb-6">
          <h1 class="mb-6 text-lg text-gray-900 font-thin">
            Đăng nhập với tài khoản của bạn
          </h1>

          <div>
            <fieldset class="mb-4">
              <label class="block text-sm text-gray-900 mb-2"
                >Tên đăng nhập</label
              >
              <input
                id="username"
                class="block w-full rounded-sm border bg-white py-2 px-3 text-sm"
                v-model="userInfo.email"
                required
              />
            </fieldset>

            <fieldset class="mb-4" @keyup.enter="login">
              <div class="w-full flex justify-between items-center">
                <label for="password" class="block text-sm text-gray-900 mb-2"
                  >Mật khẩu</label
                >
                <a
                  class="text-xs font-thin text-blue no-underline hover:underline"
                  @click="forgetPassword"
                  >Quên mật khẩu?</a
                >
              </div>
              <input
                id="password"
                type="password"
                v-model="userInfo.password"
                class="block w-full rounded-sm border bg-white py-2 px-3 text-sm"
                required
              />
            </fieldset>

            <div class="pt-1 pb-5 text-sm text-gray-darker font-thin">
              <label>
                <input class="mr-1" type="checkbox" id="remember" /> Ghi nhớ tài
                khoản
              </label>
            </div>

            <button
              @click="login"
              class="block w-full bg-blue-600 text-white rounded-sm py-3 text-sm tracking-wide"
            >
              Đăng nhập
            </button>
          </div>
        </div>

        <p class="text-center text-sm text-gray-600 font-thin">
          Bạn chưa có tài khoản.
          <a
            v-on:click="registerUser"
            class="text-blue-500 no-underline hover:underline"
            >Đăng kí tài khoản</a
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import validations from "@/utils/validations";
import { mapState, mapActions } from "vuex";
export default {
  layout: "begin",
  name: "login",
  data() {
    return {
      error: "",
      dataLogin: null,
      userInfo: {
        email: "",
        password: "",
      },
    };
  },

  methods: {
    async login() {
      this.logout();
      this.dataLogin = await this.$axios.$post(
        "http://127.0.0.1:8080/api/login",
        this.userInfo
      );
      if (this.dataLogin.error_code === 400) {
        this.$buefy.toast.open({
          message: this.dataLogin.error_message,
          type: "is-danger",
        });
      }
      if (this.dataLogin.statusCode === 200) {
        const token = this.$auth.$storage.setLocalStorage(
          "token",
          this.dataLogin.access_token
        );
        this.$axios.setHeader("Authorization", "Bearer " + token);
        const userI = {
          id: this.dataLogin.user_id,
          email: this.dataLogin.email,
        };
        this.$auth.$storage.setUniversal("user", userI, true);
        setTimeout(() => {
          this.$router.push("/docs/listdocs");
        }, 300);
      } else {
        this.error = "Tài khoản hoặc mật khẩu không đúng";
        this.$buefy.dialog.alert({
          title: "Lỗi",
          message: this.error,
          type: "is-danger",
          ariaRole: "alertdialog",
          ariaModal: true,
        });
      }
    },

    registerUser() {
      setTimeout(() => {
        this.$router.push("/register");
      }, 500);
    },
    logout() {
      this.$auth.$storage.removeUniversal("token");
      this.$auth.$storage.removeUniversal("user");
      this.$axios.setToken(null);
      this.$axios.setHeader("Authorization", null);
    },
    forgetPassword() {
      this.$router.push("/");
    },
  },
};
</script>
