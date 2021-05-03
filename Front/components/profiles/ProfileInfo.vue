<template>
  <section>
    <div>
      <b-field horizontal label="Họ">
        <b-input
          type="text"
          placeholder="Tên họ"
          v-model="userData.first_name"
        ></b-input>
      </b-field>
      <b-field horizontal label="Tên">
        <b-input
          type="text"
          placeholder="Tên"
          v-model="userData.last_name"
        ></b-input>
      </b-field>

      <b-field horizontal label="Email">
        <b-input
          type="email"
          placeholder="Email"
          v-model="userData.email"
          disabled
        ></b-input>
      </b-field>
      <b-field horizontal label="Số điện thoại">
        <b-input
          v-model="userData.phone"
          type="text"
          placeholder="Số điện thoại"
        ></b-input>
      </b-field>
      <b-field horizontal label="Đại chỉ">
        <b-input
          v-model="userData.live_at"
          type="text"
          placeholder="Địa chỉ"
        ></b-input>
      </b-field>
    </div>
    <br />
    <b-button @click="updateUser" class="is-success" style="float: right"
      >Lưu tài khoản</b-button
    >
  </section>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      userData: {},
      user: null,
    };
  },
  async created() {
    // get id user
    this.user = this.$auth.$storage.getUniversal("user");
    const id = {
      id: this.user.id,
    };
    await this.getUserById(id);
    this.userData = Object.assign({}, this.user_info);
  },
  computed: {
    ...mapState("user", ["user_info", "dataUpdate"]),
  },
  methods: {
    ...mapActions("user", ["getUserById", "updateInfoUser"]),
    async updateUser() {
      const { isSuccess } = await this.updateInfoUser(this.userData);
      if (isSuccess) {
        this.$buefy.toast.open({
          message: "Cập nhật thành công!",
          type: "is-success",
        });
      } else {
        this.$buefy.toast.open({
          message: "Cập nhật không thành công!",
          type: "is-danger",
        });
      }
    },
  },
};
</script>