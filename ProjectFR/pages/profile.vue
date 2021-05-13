<template>
  <div w-full px-6 py-12 text-left bg-gray-300 text-gray-600 leading-normal>
    <div class="is-mobile columns">
      <div class="column card">
        <b-tabs vertical>
          <b-tab-item label="Quản lí tài khoản" icon="account">
            <ProfileInfo></ProfileInfo>
          </b-tab-item>

          <b-tab-item label="Đổi mật khẩu" icon="key">
            <ChangePassWord />
          </b-tab-item>
        </b-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileInfo from "@/components/profiles/ProfileInfo.vue";
import ChangePassWord from "@/components/profiles/ChangePassword";

import { mapState, mapActions } from "vuex";
export default {
  components: {
    ProfileInfo,
    ChangePassWord,
  },
  data() {
    return {
      userData: {},
    };
  },

  methods: {},
};
</script>

<style>
.b-tabs.is-vertical > .tabs ul {
  border-right: 1px solid #dbdbdb;
  height: 600px;
}
</style>
