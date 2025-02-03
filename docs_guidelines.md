# Documentation Guidelines
If you are reading this, it means you are planning on contributing to the project, for that, we thank you.

As the project grows more and more with contributions and new API implementations, the complexity of the project increases too. For this reason we think that documenting the project is very important not only for us developers, but also for the people that will use the wrapper in their own projects.

## How to document
The project main documentation source at the moment is through Python [Docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring). They are currently implemented for classes and their respective methods, both public and private.

These docstrings are automatically parsed into the project's documentation site, so it is very important to respect the format chosen for the project.

You can find an example of a class and method here [insert link]. If you use Visual Studio Code, you can use the autoDocstring extension and set up the `autoDocstring.customTemplatePath` setting to the mustache file in the project root. This way, you will get automatic docstring generation while you code.

You can simply add this line to your `settings.json`:
```json
{
    //////////////////////////////////////
    // Your current VS Code settings... //
    //////////////////////////////////////

    // Add this line ⬇️
    "autoDocstring.customTemplatePath": "docstring.mustache"
}
```

If you use PyCharm ............

## Docstring format
We use the numpy convention with some modifications to match our needs, here are some pointers to have in mind:

- Always use double quotes for the docstrings
- Always use backticks (`) to display data types or objects
- Don't use HTML tags, or keywords enclosed by gt/lt, instead use backticks.
- Multi-line descriptions should be separated by an empty line.
- Make sure the return example is well formatted and that it is a valid JSON object or Python dict.
- Descriptions should start in the first line of the docstring, next to the quotes, and maintain the indentation thoughout the whole docstring.

You can check the example below, or some already implemented API docstrings like [Cloud Sync](https://github.com/N4S4/synology-api/blob/master/synology_api/cloud_sync.py), [ABM](https://github.com/N4S4/synology-api/blob/master/synology_api/abm.py), [User API](https://github.com/N4S4/synology-api/blob/master/synology_api/core_user.py).

If you have any doubt, don't hesitate in creating a new discussion in the repository or joining the Development Telegram Group.

## Example documentation
```python
class MyNewClass():
    """This is the main description of the class, it should be concise and to the point.

        Here is some extra information about the class.

        Supported methods:
        - Getters:
            - Get A from B
            - Get X from Y
        - Setters: 
            - Set A
            - Set X
        Actions:
            - Do something
            - Create something
            - Delete something

        See full docs:  
        https://N4S4.github.io/synology-api/docs/apis/MyNewClass
    """

    def get_a(my_arg: int, my_karg: str = "", new_karg: str = "option1"):
        """This is the main description of the method, it should be concise and to the point.

            Here is some extra information about the class.

            We can make headers (visible in the documentation site) as so:

            Info: Some information about the method usage

            Tip: A tip about how to use the method / clarification.

            Warning: A warning about this method doing some dangerous stuff.

            Parameters
            ---------
            my_arg : int
                A description about this argument.
            
            my_karg : str, optional
                A description about this argument. Defaults to `""`.

                Multiline information.
            
            new_karg : str, optional
                A description about this argument. Defaults to `"option1"`

                We can make a list of possible values too:
                - `option1` -> Does X
                - `option2` -> Does Y
                - `option3` -> Does Z

            Returns
            ----------
            dict[str, object]
                Brief description of what the return data contains.

            Example return
            ----------
            ```json
            {
                "data": {
                    "a": "the value of a"
                },
                success: true
            }
            ```
        """
```