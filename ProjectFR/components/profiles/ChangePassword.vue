
<template>
  <section>
    <div>
      <b-field horizontal label="Mật khẩu cũ">
        <b-input
          type="password"
          placeholder="Mật khẩu cũ"
          v-model="oldPassword"
        ></b-input>
      </b-field>
      <b-field horizontal label="Mật khẩu mới">
        <b-input
          type="password"
          placeholder="Mật khẩu mới"
          v-model="newPassword"
        ></b-input>
      </b-field>
      <b-field horizontal label="Xác nhận mật khẩu mới">
        <b-input
          type="password"
          placeholder="Xác nhận mật khẩu mới"
          v-model="rePassword"
        ></b-input>
      </b-field>
      <b-field>
        <div class="buttons" style="float: right">
          <b-button @click="changePW" class="is-info">Đổi mật khẩu</b-button>
        </div>
      </b-field>
    </div>
  </section>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      user: null,
      oldPassword: null,
      newPassword: null,
      rePassword: null,
    };
  },
  async created() {
    // get id user
    this.user = this.$auth.$storage.getUniversal("user");
  },
  computed: {
    ...mapState("user", ["dataChangePass"]),
  },
  methods: {
    ...mapActions("user", ["changePasswordUser"]),
    async changePW() {
      if (this.rePassword === this.newPassword) {
        const changeData = {
          id: this.user.id,
          old_password: this.oldPassword,
          new_password: this.newPassword,
        };
        const { isSuccess } = await this.changePasswordUser(changeData);
        if (isSuccess) {
          this.$buefy.toast.open({
            message: this.dataChangePass.message,
            type: this.dataChangePass.type,
          });
          if (this.dataChangePass.type === "is-success") {
            setTimeout(() => {
              this.$router.push("/");
            }, 500);
          }
        } else {
          this.$buefy.toast.open({
            message: "Có lỗi xãy ra!",
            type: "is-danger",
          });
        }
      } else {
        this.$buefy.toast.open({
          message: "Mật khẩu mới không giống nhau!",
          type: "is-danger",
        });
      }
    },
  },
};
</script>
<style scoped>
</style>