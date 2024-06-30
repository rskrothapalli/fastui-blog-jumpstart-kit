from fastui import components as c
import plotly.express as px

def show_interactive_chart():
    df = px.data.gapminder()
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
            size="pop", color="continent", hover_name="country",
            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

    fig["layout"].pop("updatemenus") # optional, drop animation buttons
    return fig.to_html()

def get_output():
    return [
    c.Heading(text='Hello! Welcome to python post', level=5, class_name='+ py-4'),
    c.Iframe(srcdoc=show_interactive_chart(), src='https://dummy.test.silly.link', width='100%', height='600px'),
    ]