import {
  FormControl,
  FormControlLabel,
  FormLabel,
  Radio,
  RadioGroup
} from "@material-ui/core";
import React, { useState } from "react";

function Themes({stateValue, changeStateValue}) {
  const [value, setValue] = useState(stateValue);

  const handleChange = e => {
    setValue(e.target.value);
    changeStateValue(e);
  }

  return (
    <FormControl component="fieldset">
      <FormLabel component="legend">Theme</FormLabel>
      <RadioGroup name="theme" value={value} onChange={handleChange}>
        <FormControlLabel value="light" control={<Radio />} label="Light" />
        <FormControlLabel value="dark" control={<Radio />} label="Dark" />
      </RadioGroup>
    </FormControl>
  );
}

export default Themes;