<template>
  <div class="menu">
    <b-menu class="menun">
      <b-menu-list label="Menu">
        <b-menu-item
          icon="account-box-multiple"
          label="Tài khoản người dùng"
          @click="listUsers"
        ></b-menu-item>
        <b-menu-item
          icon="account-box-multiple"
          label="Tài khoản admin"
          @click="listAdmins"
        ></b-menu-item>
        <b-menu-item
          icon="animation-outline"
          label="Thể loại"
          @click="listCategory"
        >
        </b-menu-item>
      </b-menu-list>
      <b-menu-list label="Actions">
        <b-menu-item icon="logout" label="Logout" @click="logout"></b-menu-item>
      </b-menu-list>
    </b-menu>
    <br />
  </div>
</template>
<script>
export default {
  data() {
    return {
      token: null,
    };
  },
  created() {},
  computed: {
    isLogin() {
      const user = this.$auth.$storage.getUniversal("user");
      if (!user) {
        return false;
      }
      return true;
    },
  },
  methods: {
    listUsers() {
      setTimeout(() => {
        this.$router.push("/admin/listuser");
      }, 500);
    },
    listAdmins() {
      setTimeout(() => {
        this.$router.push("/admin/listadmin");
      }, 500);
    },
    listCategory() {
      setTimeout(() => {
        this.$router.push("/admin/listcategory");
      }, 500);
    },
    logout() {
      this.$auth.$storage.removeUniversal("token");
      this.$auth.$storage.removeUniversal("user");
      this.$axios.setToken(null);
      this.$axios.setHeader("Authorization", null);
      setTimeout(() => {
        this.$router.push("/");
      }, 500);
    },
  },
};
</script>


<style scoped>
.menu {
  margin-top: 2px;
  margin-left: 4px;
  /* border-bottom: 2px solid rgba(var(--b3f, 217, 217, 217), 1); */
  height: 490px;
  /* border-radius: 2% 6% 5% 4% / 1% 1% 2% 4%; */
}
.menun {
  /* border-right: 2px solid rgba(var(--b3f, 217, 217, 217), 1); */
}
</style>

