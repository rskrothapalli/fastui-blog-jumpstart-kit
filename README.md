## How to use this jumpstart application?
The configuration file for customizing the application can be found at app/blog.yml. This file controls the setup for the entire blog. You can add sections for new posts under the articles section and utilize the status flag to designate the posts as either `draft` mode or `published` mode.

The actual posts are stored in the `static` folder inside the app.

To run the app, ensure that you have installed all the dependencies mentioned in the `pyproject.toml` file. Navigate to the app folder and execute the following command.

```shell
python run_app.py
```
Your application will be accessible at localhost port 80.
