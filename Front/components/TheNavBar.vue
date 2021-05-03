<template>
  <div class="menu">
    <b-menu class="menun">
      <b-menu-list label="Menu">
        <b-menu-item
          icon="bookshelf"
          label="Danh sách tài liệu"
          @click="listDocs"
        ></b-menu-item>

        <b-menu-item icon="account" label="Tài khoản">
          <b-menu-item
            label="Thông tin tài khoản"
            @click="changeProfile"
          ></b-menu-item>
          <b-menu-item
            label="Đổi mật khẩu"
            @click="changeProfile"
          ></b-menu-item>
        </b-menu-item>

        <b-menu-item
          icon="trash-can-outline"
          label="Thùng rác"
          @click="listDocsDel"
        ></b-menu-item>
        <!-- </b-menu-list>
      <b-menu-list label="Actions"> -->
        <b-menu-item
          icon="logout"
          label="Đăng xuất"
          @click="logout"
        ></b-menu-item>
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
    // => list-doc
    listDocs() {
      setTimeout(() => {
        this.$router.push("/docs/listdocs");
      }, 500);
    },

    // => list-del
    listDocsDel() {
      setTimeout(() => {
        this.$router.push("/docs/trash_docs");
      }, 500);
    },

    // => profile
    changeProfile() {
      setTimeout(() => {
        this.$router.push("/profile");
      }, 500);
    },

    // => out
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

