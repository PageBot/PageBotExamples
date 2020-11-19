Publications, e.g. Book and Magazine
These are technically elements, with all their behavior, but typically
they are not placed in a layout. Instead they contain a set of pages,
that get transfered to a new created Document during composition.

    from pagebot.publications import Magazine, Specimen

    class FashionMagazine(Magazine):
        pass

        fm = FashionMagazine('myFile.md')
    fm.export('MyMagazine.pdf')

    class MyVariableSpecimen(Specimen):
                pass

    fm = FashionMagazine('myDataMarkDown.md')
    fm.export('MySpeciment.pdf')
