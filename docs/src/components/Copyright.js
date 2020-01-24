import React from "react";
import { Typography, Link } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

export default function Copyright() {
  const useStyles = makeStyles(theme => ({
    copyright: {
      margin: theme.spacing(3)
    }
  }));

  const classes = useStyles();
  return (
    <Typography
      variant="body2"
      color="textSecondary"
      align="center"
      className={classes.copyright}
    >
      {"Copyright © "}
      <Link color="inherit" href="https://markpatricio.com/">
        pptxtract-hymns
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}
