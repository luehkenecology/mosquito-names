# European Mosquito Names Database

An interactive web application displaying the etymology and descriptions of European mosquito species names.

## 🦟 About

This database contains information extracted from Keith R. Snow's series "The names of European mosquitoes" published in the European Mosquito Bulletin (1999-2002). Each entry includes:

- **Mosquito Name and First Describer** - Scientific name with author and year
- **Full Reference** - Complete bibliographic citation of the original description
- **Etymology** - Latin/Greek word origins and meanings
- **Full Description** - Detailed explanation of how each name was derived

## 🌐 Live Demo

Visit the app at: `https://[your-username].github.io/mosquito-names/`

## 🚀 Deployment

This app uses [Shinylive](https://shiny.posit.co/py/docs/shinylive.html) to run entirely in the browser (no server required) and is deployed to GitHub Pages.

### To deploy your own copy:

1. Fork this repository
2. Go to repository **Settings** → **Pages**
3. Under "Build and deployment", select **GitHub Actions**
4. Push to the `main` branch to trigger deployment

### Local Development

```bash
# Install dependencies
pip install shiny pandas

# Run locally
shiny run app.py
```

### Build static site locally

```bash
pip install shinylive
shinylive export . _site
# Serve locally: python -m http.server -d _site
```

## 📊 Data

The CSV data (`mosquito_names_table.csv`) contains 109 entries covering:
- Genera: Anopheles, Aedes, Culex, Coquillettidia, Culiseta, Orthopodomyia, Uranotaenia, Ochlerotatus
- Subgenera: Cellia, Finlaya, Stegomyia, Neoculex, Maillotia, and more
- Individual species with full etymological information

## 📚 Source

Snow, K.R. (1999-2002). The names of European mosquitoes: Parts 1-11. European Mosquito Bulletin, Issues 3-13. Journal of the European Mosquito Control Association.

## 📄 License

Data compiled from published scientific literature for educational purposes.
