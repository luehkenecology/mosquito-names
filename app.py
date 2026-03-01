from shiny import App, ui, render, reactive
import pandas as pd
from pathlib import Path

# Read the CSV data (resolve path relative to this file for Shinylive)
app_dir = Path(__file__).parent
df = pd.read_csv(app_dir / "mosquito_names_table.csv")

app_ui = ui.page_fluid(
    ui.panel_title("European Mosquito Names Database"),
    ui.markdown("""
    **Source:** Keith R. Snow, "The names of European mosquitoes" series, 
    European Mosquito Bulletin (1999-2002)
    """),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_text("search", "Search:", placeholder="Enter species name..."),
            ui.hr(),
            ui.markdown(f"**Total entries:** {len(df)}"),
            ui.download_button("download_data", "Download CSV"),
            width=300
        ),
        ui.card(
            ui.card_header("Mosquito Names Table"),
            ui.output_data_frame("table")
        )
    ),
    ui.card(
        ui.card_header("Selected Entry Details"),
        ui.output_ui("details")
    )
)


def server(input, output, session):
    @reactive.calc
    def filtered_data():
        data = df.copy()
        search_term = input.search().lower()
        
        if search_term:
            # Search only in the first column (Mosquito Name and First Describer)
            first_col = data.columns[0]
            mask = data[first_col].astype(str).str.lower().str.contains(search_term)
            data = data[mask]
        
        return data.reset_index(drop=True)

    @render.data_frame
    def table():
        return render.DataGrid(
            filtered_data(),
            selection_mode="row",
            height="500px",
            width="100%"
        )

    @render.ui
    def details():
        selected = table.cell_selection()
        if selected and "rows" in selected and len(selected["rows"]) > 0:
            row_idx = list(selected["rows"])[0]
            data = filtered_data()
            if row_idx < len(data):
                row = data.iloc[row_idx]
                return ui.div(
                    ui.h4(row["Mosquito Name and First Describer"]),
                    ui.hr(),
                    ui.h5("Full Reference:"),
                    ui.p(row["Full Reference"]),
                    ui.h5("Etymology:"),
                    ui.p(row["Etymology (Latin/Greek)"]),
                    ui.h5("Description:"),
                    ui.p(row["Full Description"]),
                    style="padding: 15px; background-color: #f8f9fa; border-radius: 5px;"
                )
        return ui.p("Select a row to see full details", style="color: #888; font-style: italic;")

    @render.download(filename="mosquito_names.csv")
    def download_data():
        yield filtered_data().to_csv(index=False)


app = App(app_ui, server)
