<template>
  <b-field horizontal :label="label">
    <button
      class="button"
      style="text-align:left;white-space: normal;height:auto"
      v-if="!this.isEditing"
      @click="edit()"
    >{{content}}</button>
    <div v-if="this.isEditing" style="min-width:200px;max-width:360px">
      <slot></slot>
      <!-- <b-button class="is-success" size="is-small" @click="submit()">✔</b-button> -->
      <b-button class="is-danger" size="is-small" @click="discard()">✖</b-button>
    </div>
  </b-field>
</template>
<script>
export default {
  props: {
    label: String,
    content: {
      type: String,
      default: "Unknown!"
    },
    submit: {
      type: Function,
      required: true
    }
  },
  data: function() {
    return {
      isEditing: false
    };
  },
  methods: {
    edit: function() {
      this.isEditing = true;
    },
    discard: function() {
      this.isEditing = false;
    }
  }
};
</script>