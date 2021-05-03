<template>
  <div>
    <b-field
      style="padding-left:0px"
      v-for="(val, id) in valueList"
      :content="(val, idx)"
      :key="(val, idx)"
    >
      <b-input :value="val"></b-input>
      <!-- Remove button -->
      <button class="button" style="font-weight:bold" @click="remove(id)">{{ removeBtnLabel }}</button>
      <!-- Add button -->
      <button class="button" style="font-weight:bold" @click="add(id)">{{ addBtnLabel }}</button>
    </b-field>
  </div>
</template>
<script>
export default {
  components: {},
  props: {
    addBtnLabel: {
      type: String,
      default: "+"
    },
    removeBtnLabel: {
      type: String,
      default: "−"
    },
    valueList: {
      type: Array
    }
  },
  data: function() {
    return {};
  },
  methods: {
    add: function(id) {
      // add an empty object to list
      this.valueList.splice(id + 1, 0, "");
    },
    remove: function(id) {
      // remove an object at {id} from list
      this.valueList.splice(id, 1);
      if (this.valueList.length == 0) {
        this.add(); // There must be at least 1 element in the list
      }
    }
  }
};
</script>