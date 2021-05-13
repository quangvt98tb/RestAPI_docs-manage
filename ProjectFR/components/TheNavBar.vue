<template>
  <div class="menu">
    <b-menu class="menun">
      <b-menu-list label="Menu" v-if="isUser">
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

      <b-menu-list label="Menu" v-if="!isUser">
        <b-menu-item
          icon="account-box-multiple"
          label="Tài khoản người dùng"
          @click="listUsers"
        ></b-menu-item>
        <b-menu-item
          icon="account-box-multiple"
          label="Tài khoản đã khóa"
          @click="listblUsers"
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
        <b-menu-item icon="comment" label="Bình luận" @click="listComments">
        </b-menu-item>

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
      isUser: true,
      user: null,
    };
  },
  created() {
    this.user = this.$auth.$storage.getUniversal("user");
    if (!this.user.email) {
      this.$router.push("/");
    }
    if (this.user.role_id === 0) {
      this.isUser = false;
    }
  },
  // computed: {
  //   isLogin() {
  //     const user = this.$auth.$storage.getUniversal("user");
  //     if (!user) {
  //       return false;
  //     }
  //     return true;
  //   },
  // },
  methods: {
    // => list- user
    listUsers() {
      setTimeout(() => {
        this.$router.push("/admind/listuser");
      }, 500);
    },
    // listblUsers
    listblUsers() {
      setTimeout(() => {
        this.$router.push("/admind/listuserblock");
      }, 500);
    },
    // => list-admin
    listAdmins() {
      setTimeout(() => {
        this.$router.push("/admind/listadmin");
      }, 500);
    },
    // => list-category
    listCategory() {
      setTimeout(() => {
        this.$router.push("/admind/listcategory");
      }, 500);
    },
    // => list-comment
    listComments() {
      setTimeout(() => {
        this.$router.push("/admind/listcomment");
      }, 500);
    },
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

