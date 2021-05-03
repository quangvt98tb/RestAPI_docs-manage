<template>
  <div class="is-multiline" style="min-width:200px;max-width:360px">
    <b-select placeholder="Select country" expanded>
      <option v-for="option in countries" :value="option.id" :key="option.id">{{ countries }}</option>
    </b-select>
    <b-select placeholder="Select state" expanded>
      <option v-for="option in provinces" :value="option.id" :key="option.id">{{ provinces }}</option>
    </b-select>
    <b-select placeholder="Select province" expanded>
      <option v-for="option in provinces" :value="option.id" :key="option.id">{{ provinces }}</option>
    </b-select>
    <b-select placeholder="Select city" expanded>
      <option v-for="option in cities" :value="option.id" :key="option.id">{{ cities }}</option>
    </b-select>
    <b-select placeholder="Select district" expanded>
      <option v-for="option in districts" :value="option.id" :key="option.id">{{ districts }}</option>
    </b-select>
    <b-select placeholder="Select ward" expanded>
      <option v-for="option in wards" :value="option.id" :key="option.id">{{ wards }}</option>
    </b-select>
    <b-select placeholder="Select street" expanded>
      <option v-for="option in streets" :value="option.id" :key="option.id">{{ streets }}</option>
    </b-select>
    <b-input placeholder="Detail address...">{{ details }}</b-input>
  </div>
</template>
<script>
import FieldEdit from "@/components/inputs/FieldEdit.vue";
export default {
  components: {
    FieldEdit
  },
  props: {
    label: String,
    content: String,
    submit: {
      type: Function,
      required: true
    }
  },
  data: function() {
    return {
      countries: {},
      states: {
        // TODO: Same as above.
      },
      provinces: {
        // TODO: Same as above.
      },
      cities: {
        // TODO: Same as above.
      },
      districts: {
        // TODO: Same as above.
      },
      wards: {
        // TODO: Same as above.
      },
      streets: {
        // TODO: Same as above.
      },
      details: String
    };
  },
  methods: {}
};
</script>