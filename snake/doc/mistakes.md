<h1>Mistakes</h1>

❌ **Mistake:** Terminal exit immediately, game window shut up immediately!
> 👌 **Reasong:** Choose the python interpreter as pythonw.exe, there is error in code(fine not found)
> ✔️ **Solution:** choose python.exe as interpreter, fix file not found issue. 

❌ **Mistake:** the random Apple possition is out of the window!
> 👌 **Reasong:** local appsuper.py define the width=800, height=600
> ✔️ **Solution:** change back to 640, 480

```py
# figure it out by
print(Game.screen.get_size())
```