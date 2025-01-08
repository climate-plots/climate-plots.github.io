// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-atmosphere",
          title: "atmosphere",
          description: "Atospherice indices",
          section: "Navigation",
          handler: () => {
            window.location.href = "/atmosphere/";
          },
        },{id: "nav-ocean",
          title: "ocean",
          description: "Ocean indices",
          section: "Navigation",
          handler: () => {
            window.location.href = "/ocean/";
          },
        },{id: "nav-sea-ice",
          title: "sea ice",
          description: "Sea ice indices",
          section: "Navigation",
          handler: () => {
            window.location.href = "/sea-ice/";
          },
        },{id: "news-a-simple-inline-announcement",
          title: 'A simple inline announcement.',
          description: "",
          section: "News",},{id: "news-a-long-announcement-with-details",
          title: 'A long announcement with details',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_2/";
            },},{id: "news-a-simple-inline-announcement-with-markdown-emoji-sparkles-smile",
          title: 'A simple inline announcement with Markdown emoji! :sparkles: :smile:',
          description: "",
          section: "News",},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{id: "projects-atlantic-multidecadal-oscillation",
          title: 'Atlantic Multidecadal Oscillation',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/AMO/";
            },},{id: "projects-antarctic-sea-ice-extent",
          title: 'Antarctic sea ice extent',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Antarctic_SIE/";
            },},{id: "projects-arctic-sea-ice-extent",
          title: 'Arctic sea ice extent',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Arctic_sea_ice/";
            },},{id: "projects-global-sea-ice-extent",
          title: 'Global sea ice extent',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/Global_sea_ice/";
            },},{id: "projects-interdecadal-pacific-oscillation",
          title: 'Interdecadal Pacific Oscillation',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/IPO/";
            },},{id: "projects-southern-annular-mode",
          title: 'Southern Annular Mode',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/SAM/";
            },},{id: "projects-southern-oscillation-index",
          title: 'Southern Oscillation index',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/SOI/";
            },},{id: "projects-sea-surface-temperature",
          title: 'Sea Surface Temperature',
          description: "",
          section: "Projects",handler: () => {
              window.location.href = "/projects/SST/";
            },},{
        id: 'social-bluesky',
        title: 'Bluesky',
        section: 'Socials',
        handler: () => {
          window.open("climate-plots.bsky.social", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%65%64%77%61%72%64.%64%6F%64%64%72%69%64%67%65@%75%74%61%73.%65%64%75.%61%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/climate-plots", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
