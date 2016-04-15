# NDH 2k16 "Night Deamonic Heap" challenge

**Category:** Crackme

**Points:** 400

**Description:**

Welcome to hell my friend! You have to choose a team to fight against the daemon and his minions. You will have to find in his dungeon.

Will you be able to defeat the daemon and find his treasure in ``/home/my_chall_pwned/flag``.

Good Luck!

Introduction
============

This binary is listening on port ``55550``. there is no information about the
libc and only the binary is provided.

After we disassemble the source code we see that when a character is created
we have an overflow of one byte in the heap. Let's go further!

The structure of ``character`` is the following :

```
0x0  :  vtable
0x8  :  len_name
0xf0 :  name_ptr
```

The ``len_name`` is used to avoid rellocation.

The program uses it to know if the buffer to store the new name is
large enough to contain the name.

Create overlapping chunks
=========================

We can create 4 characters: ``A, B, C, D, E, F`` all of them having names of
``0x80`` bytes.

We delete ``B`` and ``C``.

We create B with exactly ``0x88`` bytes in name.

We change the name to ``"c"*0x88+"\xf0"``

And now we create a character with a name of ``0x9a`` bytes. This character will overwrite ``len_name`` of ``D``.

So now let's begin. We have to know the address of the vtable and an
address in the heap.

Leak the adresses
=================

We see in the function used for changing names that it checks if the
new name already exists before changing it.

We can change the name of ``D`` without any call to ``malloc`` because we have
control over its ``len_name``.

We try to change ``D``'s name and force it to reach the vtable of ``D``.

Then we bruteforce the ``6`` bytes of the vtable by changing ``D``'s name. if ``D`` name exists we have the next byte. We do the same with the ``name_ptr``.

Now we can create a read-anywhere gadget.

With ``B`` we change then length of ``D`` and with ``D`` we change the length of ``E``. With ``E`` we change ``F``'s ``ptr_name`` with the address of the read, then we write ``F``'s ``len_name`` and vtable.

Now with ``D`` we change ``E``'s ``ptr_name`` to the address of ``D``'s struct. We change ``E``'s ``len_name`` to ``8`` and then we change ``E``'s vtable.

Then we rename ``E`` with the vtable address so that ``D`` has a correct vtable. We call ``print all`` and we are able to read abritrarily. The result is in ``F``'s name.

With this gadget we read the address of the text section thanks to the vtable,
then the libc ``address``.

Execute a function
==================

We can create a fake vtable that contains a gadget to decrease ``esp``.

Finally we put the ROP chain just after the ``print all`` command and
it's a win! \o/
