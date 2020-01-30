import { Avatar, Button, Grid, TextField, Typography } from "@material-ui/core";
import Container from "@material-ui/core/Container";
import CssBaseline from "@material-ui/core/CssBaseline";
import { makeStyles } from "@material-ui/core/styles";

import QueueMusicIcon from "@material-ui/icons/QueueMusic";
import React from "react";
import Themes from "./Themes";
import Copyright from "./Copyright";

const useStyles = makeStyles(theme => ({
  paper: {
    marginTop: theme.spacing(8),
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(3)
  },
  submit: {
    margin: theme.spacing(3, 0, 2)
  },
  avatar: {
    margin: theme.spacing(2),
    backgroundColor: theme.palette.secondary.main
  },
  copyright: {
    margin: theme.spacing(3)
  }
}));

function MainForm() {
  const classes = useStyles();

  return (
    <Container component="main" maxWidth="xs" className="App">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar classname={classes.avatar}>
          <QueueMusicIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          pptxtract-hymns
        </Typography>
        <p>
          Extracts the texts from church powerpoint hymns, and places them into
          a new powerpoint.
        </p>
        <form className={classes.form}>
          <Grid container spacing={2}>
            <Grid item xs={12} s={12}>
              <TextField
                autoComplete="author"
                variant="outlined"
                required
                fullWidth
                id="author"
                label="Author"
                autoFocus
              />
            </Grid>
            <Grid item xs={12} s={12}>
              <TextField
                autoComplete="title"
                variant="outlined"
                required
                fullWidth
                id="title"
                label="Title"
              />
            </Grid>
            <Grid item xs={12} s={12}>
              <TextField
                autoComplete="lyrics"
                variant="outlined"
                required
                fullWidth
                multiline
                rows="18"
                id="lyrics"
                label="Lyrics"
              />
            </Grid>
            <Grid item xs={12} s={12}>
              <Themes />
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Create PowerPoint
            </Button>
          </Grid>
        </form>
        <Copyright />
      </div>
    </Container>
  );
}

export default MainForm;