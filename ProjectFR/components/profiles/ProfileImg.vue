<template>
  <section>
    <a class="image is-1by1" @click="openUploadModal">
      <img class="is-rounded" :src="avatarSrc" style="width:100%;height:100%" />
    </a>
    <b-modal
      :active.sync="isUploadActive"
      @close="closeUploadModal"
      has-modal-card
      aria-role="dialog"
      aria-modal
    >
      <div class="content">
        <p class="image is-1by1">
          <img :src="avatarPreviewSrc" />
        </p>
        <b-upload
          class="rounded"
          v-model="imageFile"
          @input="validateImage"
          style="background:#efefef"
          drag-drop
        >
          <b-icon icon="upload" size="is-large"></b-icon>
          <p>Drop your image here or click to upload</p>
        </b-upload>
      </div>
      <div class="has-text-centered">
        <b-button class="is-success" @click="updateProfileImage">Update your profile image</b-button>
      </div>
    </b-modal>
  </section>
</template>
<script>
import { mapState, mapActions } from "vuex";
export default {
  props: ["src"],
  data() {
    return {
      avatarSrc: "",
      avatarPreviewSrc: "",
      imageFile: null,
      isUploadActive: false
    };
  },
  async created() {
    await this.getUserInfo();
    const { isSuccess } = await this.getAvatarImages(this.userInfo.avatar);
    if (isSuccess) {
      this.avatarSrc = this.dataAvatarImgUrls["size120"];
    } else {
      this.avatarSrc = "/avatar_default.png";
    }
  },
  computed: {
    ...mapState("user", ["userInfo"]),
    ...mapState("image", ["dataAvatarImgIds", "dataAvatarImgUrls"])
  },
  methods: {
    ...mapActions("user", ["updateUserInfo", "getUserInfo"]),
    ...mapActions("image", ["uploadAvatarImage", "getAvatarImages"]),
    validateImage() {
      if (this.imageFile.size > 10485760) {
        // larger than 10MB (10485760 bytes) is invalid
        this.closeUploadModal();
        this.$buefy.toast.open({
          message: "Image size is too large!( > 10MB)",
          type: "is-error"
        });
      } else {
        this.avatarPreviewSrc = URL.createObjectURL(this.imageFile);
      }
    },
    openUploadModal() {
      this.avatarPreviewSrc =
        "https://cdn.shopify.com/s/files/1/0533/2089/files/placeholder-images-image_large.png";
      this.imageFile = null;
      this.isUploadActive = true;
    },
    closeUploadModal() {
      this.isUploadActive = false;
    },
    async updateProfileImage() {
      await this.uploadAvatarImage(this.imageFile); // post an image
      let userData = this.userInfo;
      userData.avatar = this.dataAvatarImgIds[0];
      await this.updateUserInfo(userData);
      this.$buefy.toast.open({
        message: "Update profile image success!",
        type: "is-success"
      });
      this.$router.go(0);
    }
  }
};
</script>