---
sidebar_position: 2
title: Docs Guidelines
---

# Documentation Guidelines
If you are reading this, it means you are planning on contributing to the project, for that, we thank you.

As the project grows more and more with contributions and new API implementations, the complexity of the project increases too. For this reason we think that documenting the project is very important not only for us developers, but also for the people that will use the wrapper in their own projects.

## How to document
The project's main documentation source at the moment is through Python [Docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring). They are currently implemented for classes and their respective methods, both public and private.

These docstrings are **automatically parsed** into the project's documentation site, so it is very important to respect the format chosen for the project.

If you use **Visual Studio Code**, we recommend using the [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) extension and set up the `autoDocstring.customTemplatePath` setting to the mustache file in the project root. This way, you will get automatic docstring generation while you code.

You can simply add this line to your [settings.json](https://code.visualstudio.com/docs/getstarted/settings#_user-settings):
```json
{
    //////////////////////////////////////
    // Your current VS Code settings... //
    //////////////////////////////////////

    // Add this line ⬇️
    "autoDocstring.customTemplatePath": "docstring.mustache"
}
```

If you use **PyCharm**, there seems to be no way so far to use a custom template for the docstrings yet, so you can copy paste the example below. Same applies for other editors/IDEs.

Further reading: [Customizable docstring generation templates - PyCharm](https://youtrack.jetbrains.com/issue/PY-12327/Customizable-docstring-generation-templates)

## Docstring format
We use the [numpy convention](https://numpydoc.readthedocs.io/en/latest/format.html) with some modifications to match our needs, here are some pointers to have in mind:

#### Spacing / Indentation
- Class descriptions should start in the _first line of the docstring_, next to the quotes, and maintain the indentation thoughout the **whole docstring**.
- _Multi-line descriptions_ should be separated by an **empty line**.
- Parameters/Returns data types and descriptions _**should not**_ be inline.
- Respect _spacing_ and _line breaks_ seen in the examples, the parser relies on the format being consistent.
- Make sure the **Return example** is well formatted and that it is a valid JSON object or Python dict.

#### Special characters
- Always use double quotes for the docstrings
- Always use backticks (`) to display data types or objects, you can use code blocks specifying the language.
- Don't use HTML tags, or keywords enclosed by gt/lt, instead use backticks.
- Sometimes, return objects contain strings with `\n` inside of them, please remove them as they may avoid the docstring to be parsed.

#### Information
- Try to keep the first line of the description brief. You can add more information in new lines.
- Use admonitions (`Note:...`, `Info:...`, `Tip:...`, `Warning:...`) to highlight information about a class, method or param. Try to not overuse them as they can become too cluttering.
- Aim to always present a brief return summary and an example showing the data returned by the method.


You can check the example below, or some already implemented API docstrings like [Cloud Sync](https://github.com/N4S4/synology-api/blob/master/synology_api/cloud_sync.py), [ABM](https://github.com/N4S4/synology-api/blob/master/synology_api/abm.py), [User API](https://github.com/N4S4/synology-api/blob/master/synology_api/core_user.py).

If you have any doubt, don't hesitate in creating a new discussion in the repository or joining the Development Telegram Group.

## Example documentation
````python
from . import base_api

class MyNewClass(base_api.BaseApi):
    """This is the main description of the class, it should be concise and to the point.

        Here is some extra information about the class.

        Supported methods:
        - Getters:
            - Get A from B
            - Get X from Y
        - Setters: 
            - Set A
            - Set X
        - Actions:
            - Do something
            - Create something
            - Delete something

        See full docs:  
        https://N4S4.github.io/synology-api/docs/apis/MyNewClass
    """
    pass

    def get_a(self, my_arg: int, my_karg: str = "", new_karg: str = "option1") -> dict[str, object]:
        """This is the main description of the method, it should be concise and to the point.

            Here is some extra information about the class.

            We can make admonitions (visible in the documentation site) as so:

            Info: Some information about the method usage

            Tip: A tip about how to use the method / clarification.

            Warning: A warning about this method doing some dangerous stuff.

            Parameters
            ----------
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
            -------
            dict[str, object]
                Brief description of what the return data contains.

            Example return
            --------------
            ```json
            {
                "data": {
                    "a": "the value of a"
                },
                success: true
            }
            ```
        """
        pass
````